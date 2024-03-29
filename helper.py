import random


def generate_random_username(length=10):
    """Generiše slučajni korisnički ID.

    Args:
        length: Dužina slučajnog korisničkog ID-a.

    Returns:
        Slučajni korisnički ID.
    """

    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join([random.choice(characters) for _ in range(length)])


def generate_random_video_id(length=10):
    """Generiše slučajni ID videozapisa.

    Args:
        length: Dužina slučajnog ID-a videozapisa.

    Returns:
        Slučajni ID videozapisa.
    """

    characters = "0123456789"
    return "".join([random.choice(characters) for _ in range(length)])
