from PIL import Image, ImageFont, ImageDraw

def combine_image(image_up, image_down, resolution_video = (1920,1080)) :
    #Create background
    final_image = Image.new('RGB', (resolution_video[1],resolution_video[0]))
    #Add images
    final_image.paste(image_up, (int((resolution_video[1]-image_up.size[0])/2),0))
    final_image.paste(image_down, (int((resolution_video[1]-image_down.size[0])/2), int(resolution_video[0]/2)))
    return final_image

def add_text_to_image(image, text_to_write, t, resolution_video = (1920,1080), change_size = False, start_size = 500 , end_size = 200, speed =50, align="left"):
    final_image_edit = ImageDraw.Draw(image)

    if change_size == True :
        size = start_size - 40*(int(t))
        size = max(end_size, size)
    else :
        size = start_size

    font_text = ImageFont.truetype("impact.ttf", size)
    w, h = final_image_edit.textsize(text_to_write, font=font_text)
    final_image_edit.text((int((resolution_video[1] - w) / 2), int((resolution_video[0] - h) / 2)), text_to_write,font=font_text, stroke_width=5, stroke_fill=(0, 0, 0), align=align)

    return image

def full_screen_image(image, resolution_video=(1920,1080)) :
    final_image = Image.new('RGB', (resolution_video[1], resolution_video[0]))
    new_height = resolution_video[0]
    image = image.resize((int(new_height * image.size[0] / image.size[1]), new_height))

    final_image.paste(image, (int((resolution_video[1]-image.size[0])/2),0))
    return final_image

def create_background(background, resolution_video = (1920,1080)) :
    final_image = Image.new('RGB', (resolution_video[1], resolution_video[0]))
    new_height = resolution_video[0]
    ratio = background.size[0] / background.size[1]
    background = background.resize((int(ratio*new_height),new_height))
    final_image.paste(background, (int(-background.size[0]/2 + resolution_video[1]/2),0))
    return final_image

def resize_images(image_list, new_height=-1, new_width=-1) :
    new_height = int(new_height)
    new_width = int(new_width)
    if new_height != -1 or new_width != -1 :
        for i in range(0,len(image_list)) :
            ratio = image_list[i].size[0]/image_list[i].size[1]
            if new_height != -1 and new_width != -1 :
                image_list[i] = image_list[i].resize((new_width, new_height))
            elif new_height != -1 :
                width_tmp = int(new_height * ratio)
                image_list[i] = image_list[i].resize((width_tmp, new_height))
            else :
                height_tmp = int(new_width / ratio)
                image_list[i] = image_list[i].resize((new_width, height_tmp))
    return image_list


def body_comp_images(img_body1, img_body2, t, background, resolution_video=(1920,1080), angle_max=10) :
    #final_image = Image.new('RGB', (resolution_video[1], resolution_video[0]))
    final_image = background.copy()
    #Calculate pos based on time of the frame
    #Formula : f(t) = c-(abs(t-0.5)*c*2)  ,  0 < t < 1 , c the middle (where they collide)
    c = resolution_video[0] / 3
    #New formula :
    if t < 0.25 :
        equation_pos = c/2 - (abs(1.8*t-0.5)* c * 1.1)
        equation_pos = min(equation_pos, (-c*2) * pow((t-0.5),2) + c/2)
    elif t >= 0.25 and t <= 0.75 :
        equation_pos = (-c*2) * pow((t-0.5),2) + c/2
    else :
        equation_pos = c/2 - (abs(1.8* t -1.1)* c * 1.1)
        equation_pos = max(equation_pos, (-c*2) * pow((t-0.5),2) + c/2)


    angle = equation_pos / c * angle_max
    pos1 = (int(0 + equation_pos - img_body1.size[0]/2), int(resolution_video[1]/2))
    pos2 = (int(resolution_video[0]/2 - equation_pos - img_body2.size[0]/2), int(resolution_video[1]/2))

    #Apply rotation
    img_body1_rot = img_body1.rotate(-angle, Image.NEAREST, expand=1)
    img_body2_rot = img_body2.rotate(angle, Image.NEAREST, expand=1)
    # Paste images
    final_image.paste(img_body1_rot, pos1, img_body1_rot)
    final_image.paste(img_body2_rot, pos2, img_body2_rot)
    return final_image
