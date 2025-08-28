import os
from dotenv import load_dotenv
from b2_storage import setup_b2

# Load environment variables
load_dotenv()

def test_backblaze():
    print("🔗 Testing Backblaze B2 connection...")
    
    try:
        b2_api = setup_b2()
        if b2_api:
            print("✅ Backblaze B2 connection successful!")
            
            # Test bucket access
            bucket = b2_api.get_bucket_by_name(os.getenv('B2_BUCKET_NAME'))
            print(f"✅ Bucket '{os.getenv('B2_BUCKET_NAME')}' accessible")
            
            return True
        else:
            print("❌ Backblaze connection failed")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_backblaze()