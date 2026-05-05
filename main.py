import os
import urllib.request
import sys

def download_file(url, filename):
    filepath = os.path.join('downloads', filename)
    
    if os.path.exists(filepath):
        print(f"Skipping {filename} (already exists)")
        return True
    
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filepath)
        print(f"Successfully downloaded {filename}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        if os.path.exists(filepath):
            os.remove(filepath)
        return False

def main():
    urls_file = 'urls.txt'
    output_dir = 'downloads'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    if not os.path.exists(urls_file):
        print(f"Error: {urls_file} not found!")
        sys.exit(1)
        
    success_count = 0
    with open(urls_file, 'r') as f:
        for line in f:
            url = line.strip()
            if not url or url.startswith('#'):
                continue
                
            filename = url.split('/')[-1]
            if '?' in filename:
                filename = filename.split('?')[0]
                
            if download_file(url, filename):
                success_count += 1
                
    print(f"Download process finished. {success_count} files processed.")

if __name__ == "__main__":
    main()
