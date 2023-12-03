from PIL import Image, ImageDraw, ImageChops
import random
#import colorsys

def random_color():
    #h = random.random()
    #s = random.random()
    #v = random.random()

    #float_rgb = colorsys.hsv_to_rgb(h, s, v)
    #rgb = [int(x  * 255 for x in float_rgb)]

    #return tuple(rgb)

    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def interpolate(start_color, end_color, factor: float):
    reciplicat = 1 - factor
    return (
        int(start_color[0] * reciplicat + end_color[0] * factor),
        int(start_color[1] * reciplicat + end_color[1] * factor),
        int(start_color[2] * reciplicat + end_color[2] * factor)
    )

def generate_art(path: str):
    target_size = 256
    scale_factor = 2
    image_size = target_size * scale_factor
    padding_px = 16 * scale_factor
    image__background_color = (0, 0, 0)
    start_color = random_color()
    end_color = random_color()
    image = Image.new('RGB', size = (image_size, image_size), color = image__background_color)

    # Let's draw some lines
    draw = ImageDraw.Draw(image)
    points = []

    # Generating of 10 random points
    for _ in range(10):
        random_point = (
            random.randint(padding_px, image_size - padding_px),
            random.randint(padding_px, image_size - padding_px)
        )
        points.append(random_point)

    # Draw a bounding box
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    #draw.rectangle((min_x, min_y, max_x, max_y), outline= (255, 0, 0))

    # Centered the image
    delta_x = min_x - (image_size - max_x)
    delta_y = min_y - (image_size - max_y)

    for i, point in enumerate(points):
        points[i] = (point[0] - delta_x // 2, point[1] - delta_y // 2)

    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    draw.rectangle((min_x, min_y, max_x, max_y), outline=(255, 0, 0))

    # Draw the points
    thickness = 0
    n_points = len(points) - 1
    for i, point in enumerate(points):

        # Overlay canvas
        overlay_image = Image.new('RGB', size=(image_size, image_size), color=image__background_color)
        overlay_draw = ImageDraw.Draw(overlay_image)

        p_start = point

        if i == n_points:
            p_end = points[0]
        else:
            p_end = points[i + 1]

        line_pos_xy = (p_start, p_end)
        #line_color = random_color()
        color_factor = i / n_points
        line_color = interpolate(start_color, end_color, color_factor)
        thickness += scale_factor
        #draw.line(line_pos_xy, fill = line_color, width = thickness)
        overlay_draw.line(line_pos_xy, fill = line_color, width = thickness)
        image = ImageChops.add(image, overlay_image)

    image = image.resize((target_size, target_size), resample = Image.ANTIALIAS)
    image.save(path)
    #image.show()
    #print('End')

#if __name__ == '__main__':
num_of_pictures = 20
print('Starting of generating...')
for i in range(num_of_pictures):
    print(f'{i+1} - generated')
    generate_art(f'Results/{i+1}.png')
print('\nAll work done\n')