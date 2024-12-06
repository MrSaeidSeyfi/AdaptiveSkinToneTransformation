import argparse
from src.utils import load_image, save_image
from src.skin_detection import detect_skin
from src.tone_adjustment import adjust_skin_tone
from src.color_transfer import transfer_skin_color

def main():
    parser = argparse.ArgumentParser(description="Adaptive Skin Tone Transformation")
    parser.add_argument("--mode", type=str, required=True, choices=["adjust", "transfer"], 
                        help="Mode: 'adjust' for adjusting tone, 'transfer' for transferring skin color between images.")
    parser.add_argument("--input", type=str, required=True, help="Path to input image.")
    parser.add_argument("--output", type=str, required=True, help="Path to output image.")
    parser.add_argument("--tone", type=str, help="Skin tone to adjust to: black, dark, brown, olive, light, yellow")
    parser.add_argument("--target", type=str, help="Target image for color transfer.")

    args = parser.parse_args()

    if args.mode == "adjust":
        if not args.tone:
            raise ValueError("For 'adjust' mode, you must specify --tone")
        img = load_image(args.input)
        skin, mask = detect_skin(img)
        result = adjust_skin_tone(img, mask, args.tone.lower())
        save_image(result, args.output)
        print("Skin tone adjusted and image saved.")

    elif args.mode == "transfer":
        if not args.target:
            raise ValueError("For 'transfer' mode, you must specify --target")
        source_img = load_image(args.input)
        target_img = load_image(args.target)
        result = transfer_skin_color(source_img, target_img)
        save_image(result, args.output)
        print("Skin color transferred and image saved.")

if __name__ == "__main__":
    main()
