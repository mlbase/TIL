# git이란?

### 분산 버전 관리시스템

- 변경사항만을 저장
- git을 이용한 저장 서비스 제공 플랫폼(gitlab, github, bitbucket)

---

### 명령어(CLI - command - Line - Interface)

- git bash here \-

---

### unix/linux 명령어

- 현재위치의 폴더 파일 목록보기 ls
- 현재 위치 이동하기 cd <path>
- 폴더 생성하기 mkdir <name>
- 파일 생성하기 touch <name>
- 삭제하기 rm <name> (file)/ rm -r <name>(folder)

---

# git 기본기

## repository

- `git init` 명령어로 로컬 저장소 만듬
- **.git** 폴더에 git으로 버전관링 필요한 모든것이 들어 있음
- `git status`를 입력하면 현재 **staging**된 파일 목록을 확인할 수 있음

## 프로젝트 관리

- 특정 버전으로 남긴다 **"Commit"**한다
- `git add`를 통해 **staging area** 에 파일을 업로드 함(버전화)
- `git add.`을 통해 *directory*안에 모든 파일을 업로드 가능
- `git commit -m "commit_message"`을 통해 **repository**에 최종적으로 버전을 저장함.

---

### 커밋의 동작 원리

- working directory - 현재 작업을 하고 있는 directory / untracked(git으로 감시되지 않음)
- Staging Area - **commit** 으로 관리하고싶은 버전이 남아있는 곳

- repository - **comit**들이 저장되는 곳
- `git init` -> `git add` -> `git commit -m "commit_message"`
- 

---

### git 명령어들

- `git bash`

- `git add`

- `git status`

- `git config --user.email` "깃허브 가입시 이메일"

- `git config --user.name`  "깃허브 이름"

- `git log`를 통해 커밋된 버전을 확인 가능

- `git diff` 두 git commit간 차이 보기

  

---

# github 시작해보기

### github repository 와 local repository 연결

- `git remote add origin {remote_repo}` 원격 레포짓토리에 올리기
- `git push -u origin master`
- `git clone {remote_repo}` remote repo를 local로 복사합니다.

---

# Today I Learned (TIL)

- 매일 내가 배운것을 문서화 하기
- github 관리의 첫걸음