# path의 종류

### 절대 경로와 상대 경로

- 절대 경로 예시) **C:\\~ \\~\\~\\** 
- 상대경로 예시)  **cd .. , cd desktop**
-  bash에서 '~' 의 의미 : tilda (cmd 킬때 처음 나오는 위치**C:\\user\\username**)

---

# github

- `git pull origin branch`
- `git push origin branch`

- `git clone (repo-urls.git)`
- `git remote add orgin (repo-urls.git)`
- 파일이 변경되었을경우에  push 하기전반드시 pull을 해줄것 그래야 conflict가 안발생함

- add 취소하기 - > `git restore --staged (file)`

- `git restore (file)` -> commit된 상태로 파일을 되돌림

- `git reset --hard {c_id}` -> commit상태를 특정버전으로 되돌림

## commit 되돌리기

|       |  WD  |  SA  |  RP  |
| :---: | :--: | :--: | :--: |
| SOFT  |  X   |  X   |  O   |
| MIXED |  X   |  O   |  O   |
| HARD  |  O   |  O   |  O   |



- O : 과거 커밋의 모습으로 돌아갑니다

- X: 현재 내가 작업하고 있는모습이 그대로 남아 있습니다.



## gitignore 파일

- 버전관리에서 제외할 파일이름을 파일에 적으면 git이 무시함

- \* . (확장자명) -> 확장자명이 같은 파일은 깃이 관리하지 않음
- /(디렉토리이름) -> 디텔토리안에있는 모든파일은 git이 관리하지 않음
- !(파일).png -> 모든 png는 빼고 (파일).png는 넣고
- gitignore.io에 들어가면 개발환경에 맞는 gitignore 파일 생성가능

# branch - > 특정 커밋을 가르키는 '포인터'

1. `git branch {branch_name}` : 새로운 브랜치 형성
2. `git branch ` 현재 브랜치 이름
3. `git checkout {branch_name}`: 특정 브랜치로 이동
4. `git push origin {branch_name}` : 브랜치이름으로 push

5. `git branch -d {branch name}` : 브랜치 삭제
6. `git merge {branch_name}` : 머지할 브랜치를 접속한 브랜치로 합병

## branch merge

- **중요 ** : 브랜치를 너무 많이 갈랫길로 하는것보다 적당히 만들고 바로 마스터 브랜치로 병합하는게 좋음

# Git flow

- master 
- develop - 피처 브랜치 머지해서 반영해봄
- feature branches - 기능별 개발
- realease branch - 배포직전 브랜치
- hotfix branch - 급히 고쳐야할 경우 사용하는 브랜치

## 협력 모델

1. shared Repository model
2. Fork & pull Model -> 따로 repository를 만들어서 push 함

3. fork 할 repository 에서 포크하고 -> 본인 fork repository로 이동 -> init add push 하고 pull request(본인 repo에서)

