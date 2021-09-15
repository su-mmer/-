# 운영체제 기능 수행 모듈
import os
# 해싱 모듈
import hashlib

# 파일 위치
inspect_file = './eicar.txt'

# 바이러스 파일 유무 확인
if os.path.isfile(inspect_file):

    # 텍스트파일 문자열 가져오기
    fp = open(inspect_file)
    fread = fp.read()
    fp.close()

    # 파일 해시화
    hash = hashlib.md5()
    hash.update(fread.encode('utf-8'))
    md5 = hash.hexdigest()

    # 바이러스 확인
    if md5 == '44d88612fea8a8f36de82e1278abb02f':
        print("바이러스가 검출 되었습니다.")
        # 파일 삭제
        os.remove(inspect_file)
    else:
        print("바이러스가 검출 되지 않았습니다.")

else:
    print("검사할 파일이 존재하지 않습니다.")
