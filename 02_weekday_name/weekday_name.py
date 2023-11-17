def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    
    weekday_names = (None, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                     "Saturday")
    if day_of_week < 8:
        return weekday_names[day_of_week]
    else:
        return None