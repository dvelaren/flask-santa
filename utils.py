from constants import valid_user_fields


def find_modify_user(user_id, users, user_new_props=None):
    """
    Finds a user by their ID from a list of users. (Optional) Updates the user's properties if user_new_props is provided.

    Args:
        user_id (int): The ID of the user to find.
        users (list): A list of user dictionaries, where each dictionary contains user information.
        user_new_props (dict): A dictionary of new user properties to update.

    Returns:
        dict or None: The user dictionary if found, otherwise None.
    """
    for user in users:
        if user["id"] == user_id:
            if user_new_props is not None and all(
                keys in valid_user_fields for keys in user_new_props
            ):
                user.update((k, v) for k, v in user_new_props.items())
            return user
    return None
