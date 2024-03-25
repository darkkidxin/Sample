import os
from music_tag import load_file
import pandas as pd

# 指定待处理的文件夹路径
folder_path = input("Please enter folder path: ")
print(folder_path)
folder_path = f'{folder_path}'
# folder_path=r'E:\test'
audio_type_list = ['.wav','.mp3','.flac','.m4a']
# list_data = pd.DataFrame(columns=['Artist','Album','Tracknumber','Title','Year'])

def check_combied_name(one_data,input_value):
    global separator
    try:
        cutted_list = input_value.split('+')
        if len(cutted_list)>1:
            combined_list = []
            for n in range(len(cutted_list)):
                combined_list.append(one_data[int(cutted_list[n])])
            print(combined_list)
            if runtime == 1:
                judge_separator = input('需要分隔符吗？y/n\n')
                if judge_separator == "y":
                    judge2_separator = input("请输入分隔符，默认空格")
                    if judge2_separator == "":
                        separator = " "
                    else:
                        separator = judge2_separator
                        # print(f'1stseparator: {separator}')
                else:
                    separator = ""
                    # print(f'2ndseparator: {separator}')
            else:
                separator = separator
                # print(f'3ndseparator: {separator}')
            cutted_value = separator.join(combined_list)
        else:
            cutted_value = one_data[int(cutted_list[0])]
    except:
        cutted_value = one_data[int(cutted_list[0])]

    # print(f'Cutted:{cutted_value}')
    return(cutted_value)

runtime = 1
# 遍历文件夹中的 WAV 文件
for filename in os.listdir(folder_path):
    try:
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, filename)
        file_basename = os.path.basename(file_path) #去除文件夹部分
        file_name, file_extension = os.path.splitext(file_basename) #将文件名与文件类型分开
    except:
        pass
    
    if filename.endswith(file_extension) and file_extension in audio_type_list:
        print(f'当前文件名：{file_name}')
        if runtime == 1: #检查第一个文件格式，后续通用
            cut_icon = input('输入分隔符：')
            try:
                cutted_filename = file_name.split(cut_icon)
                for i in range(len(cutted_filename)):
                    print(f'[{i}]:{cutted_filename[i]}')
                input_artist_number = input('请输入Artist对应的数字，以“+”分割')
                input_album_number = input('请输入Album对应的数字，以“+”分割')
                input_title_number = input('请输入Title对应的数字，以“+”分割')
                new_album_year = input('请输入专辑年份: ')

                title_part = check_combied_name(cutted_filename,input_title_number)
                print(f'当前Title部分：{title_part}')
                judge_combine_track = input(f'是否可以直接获取？y/n\n')
                if judge_combine_track == "n":
                    cut_icon2 = input('输入分隔符：')
                    cutted_part = title_part.split(cut_icon2)
                    for i in range(len(cutted_part)):
                        print(f'[{i}]:{cutted_part[i]}')
                    track_number = input('请输入Track对应的数字')
                    
            except:
                pass
        else:
            cutted_filename = file_name.split(cut_icon)
            title_part = check_combied_name(cutted_filename,input_title_number)
            cutted_part = title_part.split(cut_icon2)

        new_artist = check_combied_name(cutted_filename,input_artist_number)
        print(f'artist: {new_artist}')
        new_album = check_combied_name(cutted_filename,input_album_number)
        print(f'album: {new_album}')
        new_tracknumber = cutted_part[int(track_number)]
        print(f'tracknumber: {new_tracknumber}')
        try:
            title_part_list = []
            for n in range(int(track_number)+1,len(cutted_part)):
                title_part_list.append(cutted_part[n])
            new_title = cut_icon2.join(title_part_list)
        except:
            new_title = title_part
        # new_title = check_combied_name(title_part,title_number)
        print(f'title: {new_title}')
        # input('pause')
        
        audio = load_file(file_path)

        # # 打印当前标签信息
        # print("Title:", audio['title'])
        # print("Artist:", audio['artist'])
        # print("Album:", audio['album'])

        # 修改标签信息
        audio['artist'] = new_artist
        audio['album'] = new_album
        audio['tracknumber'] = new_tracknumber
        audio['title'] = new_title
        audio['year'] = new_album_year

        # 保存修改后的标签信息
        audio.save()
        runtime+=1

        # # 重新加载文件并打印修改后的信息
        # audio = load_file(file_path)
        # print("Modified Title:", audio['title'])

        # file_data = pd.DataFrame.from_dict([{
        #     'Artist':new_artist,
        #     'Album':new_album,
        #     'Tracknumber':new_tracknumber,
        #     'Title':new_title,
        #     'Year':new_album_year
        #     }])
        # list_data = pd.concat([list_data,file_data],ignore_index=True)
        
# print(list_data)

input("标签信息已更新完成。回车关闭")
