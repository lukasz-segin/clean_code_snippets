import re


def read_file(file_name):
    """
    Reading file line after line.
    """

    with open(file_name) as fread:
        for line in fread:
            yield line


def get_unique_emails(file_name):
    """
    Read unique email addresses.
    """

    emails = set()
    for line in read_file(file_name):
        match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        for email in match:
            emails.add(email)
    return emails
