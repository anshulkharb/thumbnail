import os, json
from random import randint 




def generate_thumbnail(input, output, options):
    try:
        if os.path.isfile(input):
            pass
        else:
            raise('Error!')
    except:
        print("Input File doesn't exist.")
        return False
    
    try:
        if os.path.isdir(output.rsplit('/', 1)[0]):
            pass
        elif len(output.rsplit('/', 1)) == 1:
            pass
        else:
            raise('Error!')
    except:
        print("Output directory doesn't exist.")
        return False
    
    if type(options) is dict:
        options = options
    else:
        options = {}
    
    input_ext = os.path.splitext(input)[1].replace('.', '')
    output_ext = os.path.splitext(output)[1].replace('.', '')

    def has_key(dict, key):
        return True if key in dict else False
    
    options['type'] = options['type'] if has_key(options, 'type') else 'thumbnail'
    options['width'] = str(options['width']) if has_key(options, "width") else '300'
    options['height'] = str(options['height']) if has_key(options, "height") else '300'
    options['quality'] = str(options['quality']) if has_key(options, "quality") else '85'

    if has_key(options, 'trim'):
        if options['trim'] is True:
            options['trim'] = '-trim'
        else:
            options['trim'] = ''
    else:
        options['trim'] = ''


    if options['type'] == 'thumbnail':
        imgcommand = '-geometry '+options['height']+' -extent '+options['width']+'X'+options['height']
        vidcommand = ''
    elif options['type']:
        imgcommand = ''
        vidcommand = ''
    
    # print(options)

    # print(input_ext, output_ext)
    
    try:
        if output_ext in ['png', 'jpg', 'gif']:
            pass
        else:
            raise('Error!')
    except:
        print('Output extension is not supported.')
        return False
    
    mimedb_path = os.path.dirname(os.path.realpath(__file__)) + '/mimedb.json'
    with open(mimedb_path) as json_file:
        mimedb = json.load(json_file)
    # print(mimedb[0])

    for k in mimedb:
        if 'extensions' in mimedb[k]:
            for e in mimedb[k]['extensions']:
                if e == input_ext:
                    if k.split('/')[0] == 'image':
                        filetype = 'image'
                    elif k.split('/')[0] == 'video':
                        filetype = 'video'
                    else:
                        filetype = 'other'
                    pass
    
    try:
        filetype
    except:
        print('Input file is not supported.')
        return False
    
    if output_ext == 'pdf':
        filetype = 'image'
    
        
    if filetype == 'video':
        command = 'ffmpeg -y -i '+input+' -vf thumbnail '+vidcommand+' -frames:v 1 '+output
        # print(command)
        os.system(command)
    elif filetype == 'image':
        command = 'convert '+options['trim']+' -quality '+options['quality']+' '+imgcommand+' -colorspace RGB '+input+'[0] '+output
        os.system(command)
    elif filetype == 'other':

        tmppath = './' + str(randint(1000, 9999)) + '.pdf'
        command = 'unoconv -e PageRange=1 -o '+tmppath+' '+input
        os.system(command)
        command = 'convert '+options['trim']+' -quality '+options['quality']+' '+imgcommand+' -colorspace RGB '+tmppath+'[0] '+output
        # print(command)
        os.system(command)
        os.remove(tmppath)
        
    return True