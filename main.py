"""
This script removes the background from images using the Azure AI Vision SDK.
"""
import json
import os
import azure.ai.vision as sdk

def configure():
    """
    Reads the configuration from a JSON file named 'config.json' located in the same directory.
    
    Returns:
        dict: The configuration settings loaded from the JSON file.
    """
    with open('config.json', 'r', encoding='utf-8') as f:
        config_data = json.load(f)
    return config_data

def remove_background(options, source):
    """
    Removes the background from an image using Azure AI Vision SDK and saves
    the result as a PNG file.
    
    Args:
        options (sdk.ImageAnalysisOptions): The options for image analysis.
        source (str): The file path of the source image.
    
    Returns:
        None
    """

    output_image_file = f"./output/{os.path.basename(source)}.png"

    analysis_options = sdk.ImageAnalysisOptions()
    analysis_options.segmentation_mode = sdk.ImageSegmentationMode.BACKGROUND_REMOVAL

    vision_source = sdk.VisionSource(filename=source)
    image_analyzer = sdk.ImageAnalyzer(options, vision_source, analysis_options)

    result = image_analyzer.analyze()

    if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:

        image_buffer = result.segmentation_result.image_buffer
        print(" Segmentation result:")
        print(f"   Output image buffer size (bytes) = {len(image_buffer)}")
        print(f"   Output image height = {result.segmentation_result.image_height}")
        print(f"   Output image width = {result.segmentation_result.image_width}")

        with open(output_image_file, 'wb') as binary_file:
            binary_file.write(image_buffer)
        print(f"   File {output_image_file} written to disk")

    else:

        error_details = sdk.ImageAnalysisErrorDetails.from_result(result)
        print(" Analysis failed.")
        print(f"   Error reason: {error_details.reason}")
        print(f"   Error code: {error_details.error_code}")
        print(f"   Error message: {error_details.message}")
        print(" Did you set the computer vision endpoint and key?")


config = configure()
service_options = sdk.VisionServiceOptions(config["endpoint"], config["key"])

for filename in os.listdir("./input"):
    print(f"Processing {filename}")
    remove_background(service_options, f"./input/{filename}")
