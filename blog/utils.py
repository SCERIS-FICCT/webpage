def event_picture_path(instance, filename):     
    # Default Path for Picture
    return 'events/{0}/{1}'.format(instance.id, filename)