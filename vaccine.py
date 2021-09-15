import os

inspect_file = './eicar.txt'

# 바이러스 파일 유무 확인
if os.path.isfile(inspect_file):

    fp = open(inspect_file)
    fread = fp.read()
    fp.close()

    # 바이러스 확인
    if fread[0:3] == 'X5O':
        print("바이러스가 검출 되었습니다.")
        # 파일 삭제
        os.remove(inspect_file)
    else:
        print("바이러스가 검출 되지 않았습니다.")

else:
    print("검사할 파일이 존재하지 않습니다.")
