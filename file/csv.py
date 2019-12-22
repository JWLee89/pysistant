import csv


def write(relative_file_path, data):
    """
        Simple function for writing to csv file
        :param relative_file_path The relative file path
        :param data The data to write. Must be an iterable dataset
    """
    with open(relative_file_path, 'w') as csv_file:
        wr = csv.writer(csv_file)
        for row in data:
            wr.writerow(row)


def read(file_path, has_header=True):
    result = []

    def handle_file_write(keys=None):
        """
            :param keys:
            :return:
        """
        cur_item = {}

        def write_with_headers(line):
            """
                In this case, each item inside of the header list
                will be the 'key' for each row

                :param line The current line that is being read
            """
            data = line.split(',')
            i = 0
            for key in keys:
                cur_item[key] = data[i].strip()
                i += 1
            result.append(cur_item)

        def write_without_headers(line):
            """
                Since there is no header, our key will simply be
                the zero-based indexes of the elements
                e.g. 0, 1, 2, 3, ... , n
                :param line The current line that is being read
            """
            data = line.split(',')
            for i in range(len(data)):
                cur_item[i] = data[i].strip()
            result.append(cur_item)

        if keys:
            return write_with_headers
        else:
            return write_without_headers

    with open(file_path, 'r') as csv_file:
        if has_header:
            header = list(map(str.strip, csv_file.readline().split(',')))
            write_for_csv_with_headers = handle_file_write(header)
            for line in csv_file:
                write_for_csv_with_headers(line)
        else:
            # Can also allow for non-equal number of data
            write_for_csv_without_headers = handle_file_write()
            for line in csv_file:
                write_for_csv_without_headers(line)
    return result


if __name__ == "__main__":
    result = read("diabetes.csv", has_header=True)
    print(result)