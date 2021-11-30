from functions.read_file_with_generator_and_process_data import get_unique_emails


def main() -> None:
    """
    Main function
    :return None:
    """

    print("Test")
    print(get_unique_emails("functions/files/emails.txt"))


if __name__ == '__main__':
    main()
