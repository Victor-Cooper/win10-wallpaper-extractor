import os,shutil,uuid

source_dir = "C:\\Users\\ShawYoung Tang\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
target_dir = "C:\\Users\\ShawYoung Tang\\Desktop\\New folder"



def get_all_file_names(dir_name):
    result = []
    for main_dir, sub_dir, file_name_list in os.walk(dir_name):
        for file_name in file_name_list:
            apath = os.path.join(main_dir, file_name)
            result.append(apath)
    return result

def copy(source, target):
	shutil.copy(source, target)


def main():
	all_file_names = get_all_file_names(source_dir)
	if not os.path.exists(target_dir):
		os.makedirs(target_dir)
	for source_file_name in all_file_names:
		dest_file_name = target_dir + "\\" + str(uuid.uuid4()) + ".jpg"
		if not os.path.exists(dest_file_name):
			copy(source_file_name, dest_file_name)

main()
