
"""
- [ ] 드론 작동여부 확인
    - [ ] zed 카메라
    - [ ] 
- [ ] 각 노드 작동여부 확인
    - [ ] zed
    - [ ] yolo
    - [ ] 이미지처리
    - [ ] 장애물 인식
    - [ ] 경로생성
    - [ ] 매핑
    - [ ] 경로생성
    - [ ] 제어노드
"""

import droneflag as df

def main():
    
    #작동시작
    df.Flags.state_missionOnGoing = True
    
    while(df.Flags.state_missionOnGoing == True):
        
    
        
    