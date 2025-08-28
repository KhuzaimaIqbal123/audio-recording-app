import b2sdk
from b2sdk.v2 import B2Api, InMemoryAccountInfo, UploadSourceBytes
import logging
import os

def setup_b2():
    """Initialize Backblaze B2 connection."""
    try:
        info = InMemoryAccountInfo()
        b2_api = B2Api(info)
        b2_api.authorize_account(
            "production", 
            application_key_id=os.getenv('B2_KEY_ID'),
            application_key=os.getenv('B2_APPLICATION_KEY')
        )
        logging.info("✅ Backblaze B2 connection established")
        return b2_api
    except Exception as e:
        logging.error(f"❌ B2 Authorization failed: {e}")
        return None

def upload_to_b2(audio_data, filename):
    """Upload audio data to Backblaze B2."""
    try:
        b2_api = setup_b2()
        bucket = b2_api.get_bucket_by_name(os.getenv('B2_BUCKET_NAME'))
        
        upload_source = UploadSourceBytes(audio_data)
        file_info = bucket.upload(
            upload_source,
            filename,
            content_type="audio/wav"
        )
        
        # Generate download URL
        download_url = b2_api.get_download_url_for_file_name(
            os.getenv('B2_BUCKET_NAME'), 
            filename
        )
        
        logging.info(f"✅ File uploaded to B2: {download_url}")
        return download_url
        
    except Exception as e:
        logging.error(f"❌ B2 upload failed: {e}")
        raise