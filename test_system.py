#!/usr/bin/env python3
"""
Quick system test for Aviation Data Warehouse
"""

import sqlite3
import os
from pathlib import Path

def test_database():
    """Test database connectivity and data"""
    try:
        db_path = 'aviation_warehouse.db'
        if not os.path.exists(db_path):
            print("❌ Database file not found!")
            return False
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        print(f"✅ Database connected successfully")
        print(f"📊 Tables found: {tables}")
        
        # Check main fact table
        if 'Fakta_Penerbangan' in tables:
            cursor.execute("SELECT COUNT(*) FROM Fakta_Penerbangan;")
            count = cursor.fetchone()[0]
            print(f"📈 Fakta_Penerbangan records: {count:,}")
            
            # Get sample data
            cursor.execute("SELECT * FROM Fakta_Penerbangan LIMIT 3;")
            sample = cursor.fetchall()
            print(f"📋 Sample data rows: {len(sample)}")
            
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def test_visualizations():
    """Check visualization files"""
    viz_dir = Path('visualizations')
    if not viz_dir.exists():
        print("❌ Visualizations directory not found!")
        return False
    
    viz_files = list(viz_dir.glob('*.png'))
    print(f"🎨 Visualization files found: {len(viz_files)}")
    
    for file in viz_files:
        file_size = file.stat().st_size
        print(f"   📊 {file.name} ({file_size:,} bytes)")
    
    return len(viz_files) > 0

def main():
    print("🧪 AVIATION DATA WAREHOUSE - SYSTEM TEST")
    print("=" * 50)
    
    print("\n1. Testing Database...")
    db_ok = test_database()
    
    print("\n2. Testing Visualizations...")
    viz_ok = test_visualizations()
    
    print(f"\n🎯 SYSTEM STATUS:")
    print(f"   Database: {'✅ OK' if db_ok else '❌ FAILED'}")
    print(f"   Visualizations: {'✅ OK' if viz_ok else '❌ FAILED'}")
    
    if db_ok and viz_ok:
        print("\n🚀 System is ready and functional!")
        return True
    else:
        print("\n⚠️ System has issues that need attention")
        return False

if __name__ == "__main__":
    main()
