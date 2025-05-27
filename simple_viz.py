#!/usr/bin/env python3
"""
Simple Visualization Generator
Menghasilkan visualisasi sederhana berdasarkan data yang ada di database
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')
plt.style.use('default')
sns.set_palette("husl")

class SimpleVisualizer:
    def __init__(self, db_path='aviation_warehouse.db'):
        self.db_path = db_path
        self.output_dir = Path('visualizations')
        self.output_dir.mkdir(exist_ok=True)
        
    def connect_db(self):
        return sqlite3.connect(self.db_path)
    
    def test_connection(self):
        """Test database connection and show table info"""
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            
            # Get table names
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]
            print(f"Available tables: {tables}")
            
            # Check Fakta_Penerbangan structure
            if 'Fakta_Penerbangan' in tables:
                cursor.execute("SELECT * FROM Fakta_Penerbangan LIMIT 3;")
                sample_data = cursor.fetchall()
                
                cursor.execute("PRAGMA table_info(Fakta_Penerbangan);")
                columns = [col[1] for col in cursor.fetchall()]
                print(f"Fakta_Penerbangan columns: {columns}")
                print(f"Sample data count: {len(sample_data)}")
                
            conn.close()
            return True
        except Exception as e:
            print(f"Database connection failed: {e}")
            return False
    
    def create_simple_charts(self):
        """Create basic charts from available data"""
        try:
            conn = self.connect_db()
            
            # Chart 1: Basic Revenue Analysis
            query1 = """
            SELECT 
                COUNT(*) as Total_Flights,
                SUM(Pendapatan) as Total_Revenue,
                AVG(Pendapatan) as Avg_Revenue,
                SUM(Jumlah_Penumpang) as Total_Passengers
            FROM Fakta_Penerbangan
            """
            
            df_summary = pd.read_sql_query(query1, conn)
            
            # Create summary chart
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
            
            # KPI Cards style visualization
            metrics = [
                ('Total Flights', df_summary['Total_Flights'].iloc[0], ax1, '#1f77b4'),
                ('Total Revenue (B)', df_summary['Total_Revenue'].iloc[0]/1e9, ax2, '#ff7f0e'),
                ('Avg Revenue (M)', df_summary['Avg_Revenue'].iloc[0]/1e6, ax3, '#2ca02c'),
                ('Total Passengers', df_summary['Total_Passengers'].iloc[0], ax4, '#d62728')
            ]
            
            for title, value, ax, color in metrics:
                ax.text(0.5, 0.5, f'{value:,.1f}', ha='center', va='center', 
                       fontsize=24, fontweight='bold', color=color)
                ax.text(0.5, 0.2, title, ha='center', va='center', 
                       fontsize=12, fontweight='bold')
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.axis('off')
                
                # Add border
                rect = plt.Rectangle((0.05, 0.1), 0.9, 0.8, fill=False, 
                                   edgecolor=color, linewidth=3)
                ax.add_patch(rect)
            
            plt.suptitle('Aviation Data Warehouse - Key Performance Indicators', 
                        fontsize=16, fontweight='bold')
            plt.tight_layout()
            plt.savefig(self.output_dir / '01_kpi_summary.png', dpi=300, bbox_inches='tight')
            plt.close()
            
            # Chart 2: Revenue Distribution by Class
            query2 = """
            SELECT 
                dk.Nama_Kelas,
                SUM(ff.Pendapatan) as Revenue,
                COUNT(*) as Flight_Count
            FROM Fakta_Penerbangan ff
            JOIN Dim_KelasLayanan dk ON ff.KelasID = dk.KelasID
            GROUP BY dk.Nama_Kelas
            ORDER BY Revenue DESC
            """
            
            df_class = pd.read_sql_query(query2, conn)
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
            
            # Pie chart
            colors = ['#ff9999', '#66b3ff', '#99ff99']
            wedges, texts, autotexts = ax1.pie(df_class['Revenue'], 
                                              labels=df_class['Nama_Kelas'],
                                              autopct='%1.1f%%',
                                              colors=colors,
                                              explode=(0.05, 0.05, 0.05))
            ax1.set_title('Revenue Distribution by Class', fontweight='bold', fontsize=14)
            
            # Bar chart
            bars = ax2.bar(df_class['Nama_Kelas'], df_class['Revenue']/1e9, color=colors)
            ax2.set_title('Revenue by Class (Billion Rp)', fontweight='bold', fontsize=14)
            ax2.set_ylabel('Revenue (Billion Rupiah)', fontweight='bold')
            ax2.tick_params(axis='x', rotation=45)
            
            for bar, value in zip(bars, df_class['Revenue']/1e9):
                ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                        f'Rp {value:.1f}B', ha='center', va='bottom', fontweight='bold')
            
            plt.tight_layout()
            plt.savefig(self.output_dir / '02_class_revenue.png', dpi=300, bbox_inches='tight')
            plt.close()
            
            # Chart 3: Delay Analysis
            query3 = """
            SELECT 
                CASE 
                    WHEN Keterlambatan <= 15 THEN 'On Time (≤15 min)'
                    WHEN Keterlambatan <= 30 THEN 'Minor Delay (16-30 min)'
                    WHEN Keterlambatan <= 60 THEN 'Moderate Delay (31-60 min)'
                    ELSE 'Major Delay (>60 min)'
                END as Delay_Category,
                COUNT(*) as Flight_Count
            FROM Fakta_Penerbangan
            GROUP BY Delay_Category
            """
            
            df_delay = pd.read_sql_query(query3, conn)
            
            plt.figure(figsize=(12, 8))
            colors = ['#2E8B57', '#FFD700', '#FF8C00', '#DC143C']
            bars = plt.bar(df_delay['Delay_Category'], df_delay['Flight_Count'], color=colors)
            
            for bar, count in zip(bars, df_delay['Flight_Count']):
                plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                        str(count), ha='center', va='bottom', fontweight='bold')
            
            plt.title('Flight Delay Analysis', fontsize=16, fontweight='bold', pad=20)
            plt.xlabel('Delay Category', fontweight='bold')
            plt.ylabel('Number of Flights', fontweight='bold')
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', alpha=0.3)
            plt.tight_layout()
            plt.savefig(self.output_dir / '03_delay_analysis.png', dpi=300, bbox_inches='tight')
            plt.close()
            
            conn.close()
            
            print("✅ Simple visualizations generated successfully!")
            print(f"📁 Charts saved in: {self.output_dir.absolute()}")
            print("\n📊 Generated Charts:")
            print("   1. 01_kpi_summary.png - Key Performance Indicators")
            print("   2. 02_class_revenue.png - Revenue by Passenger Class")
            print("   3. 03_delay_analysis.png - Flight Delay Distribution")
            
        except Exception as e:
            print(f"❌ Error generating visualizations: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    print("🎨 Starting Simple Visualization Generation...")
    print("=" * 50)
    
    visualizer = SimpleVisualizer()
    
    # Test connection first
    if visualizer.test_connection():
        print("✅ Database connection successful")
        visualizer.create_simple_charts()
    else:
        print("❌ Database connection failed")
