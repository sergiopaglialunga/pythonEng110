import csv

def transform_user_details(csv_file_name):
    new_user_data = []

    with open("user_details.csv", newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)

    return new_user_data

def create_new_user_data_csv(old_user_data_file="user_details_csv",new_file_name='new_user_data_csv'):

    new_user_data = transform_user_details(old_user_data_file)
    new_file = open(new_file_name, 'w')

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(new_user_data)

    return new_user_data