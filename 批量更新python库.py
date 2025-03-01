import os
import sys
import time

def jiancha():
    # 使用 pip 检查过时的包
    txt = 'pip list --outdated'
    li = os.popen(txt).read()
    print(li)
    
    # 询问用户是否确认更新
    f = input('是否开始更新[请输入OK]:').strip().lower()
    if f != 'ok':
        print('退出更新。')
        sys.exit()
    
    print('现在开始更新...')
    time.sleep(1)
    
    # 将输出按行拆分为单独的包信息
    li = li.split('\n')[2:]  # 跳过前两行（表头）
    
    # 遍历每个包并尝试更新
    for package_info in li:
        if not package_info.strip():
            continue  # 跳过空行
        
        # 提取包名（第一列）
        package_name = package_info.split()[0].strip()
        if not package_name:
            continue  # 跳过不包含包名的行
        
        print(f'正在更新: {package_name}')
        try:
            # 尝试更新包
            d = os.popen(f'pip install --upgrade {package_name}').read()
            print(d)
        except Exception as e:
            print(f'更新 {package_name} 时出错: {e}')
    
    print('更新完成。')

if __name__ == '__main__':
    jiancha()
