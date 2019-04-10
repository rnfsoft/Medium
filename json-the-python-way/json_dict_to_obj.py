def dict_to_obj(our_dict):
    # Funciton that taks in a dict and returns a custom object assoicated with the dict
    # This funciton makes use of the "__module__" and "__class__" in the dictionary to know which object type to create
    if "__class__" in our_dict:
        # pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name  = our_dict.pop("__class__")

        # get the module name from the dict and import it
        module_name = our_dict.pop("__module__")

        # we use the built in __import__ funciton since the module name is not yet known at runtime
        module = __import__(module_name)

        # get the class from the module
        class_ = getattr(module, class_name)

        # user dictionary unpacking to initionalize the object
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj