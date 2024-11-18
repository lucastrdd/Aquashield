from better_bing_image_downloader import downloader

downloader("Oil Spill in Water", limit=100, output_dir='testar', adult_filter_off=True,
force_replace=False, timeout=60, filter="photo", verbose=True, badsites= [], name='Image')