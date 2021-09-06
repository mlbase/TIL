# DAO와 DTO

- dto(data transfer object) - data를 저장하고 dao에 전달하는 클래스
- dto 에서 constructor -> source menu에서 생성가능
- dao(data acess object) - data를 직접 수정하는 클래스( 추가, 삭제, 검색, 수정)

- oop를 할때 캡슐화를 위해 getter와 setter 를 쉽게 설정할 수있는 메크로를 제공(generate getter/setter)

# Super class

- parents class 부터 호출하고 child class를 호출함.
- protected를 통해 parents class 변수에 접근가능

- parents class 와 child class 는 같은 메모리영역에 잡힘

- **instance**와 **parameter**가 겹치지 않으면 `.this` 생략가능

- java는 최상위 클래스 object가 존재한다. 일반적으로 `ex object`라는 표현이 모든 클래스 선언마다 생략되어있다.

- *override* : 상속받은 메서드를 고쳐기입한다.

- `instanceof` 객체의 클래스를 비교 가능

  ## 클래스 강제 형변환 

-  객체는 부모클래스 생성은 자식클래스로 생성가능 -> 이경우에는 메모리 주소가 부모클래스를 가르킴

- 다시 이 클래스 포인터를 자식클래스로 잡으면서 메모리 낭비를 막을 수 있음

  ### 클래스의 3 속성

- 은닉성(capsule)

- 상속(overried)

- 다형성

  # 변수

- 정적

- 전역

- 지역

- 멤버



### static method는 인스턴스가 아닌 클래스를 통해서 직접 호출해야됨

- subclass는 finalclass를 superclass로 상속받을수 없다.

- final method는 overriding 금지

  ## 추상클래스

- method를 아무처리없이 선언하고 subclass나 메인 함수에서 처리가능 *ex) react에서 버튼*

  ---

  # interface

- abstract class : 일반 멤버 메서드 + 일반 멤버변수 + 추상 메서드
-  interface : 추상 메소드, 선안만 되어 있는 비어 있는 클래스 메소드의 타입만이 설정되어 있다. 
- 다중 상속이 가능하다. (**원래 자바에서는 다중상속 클래스 불가능**)
- 빠르게 클래스의 사양을 파악할 수 있다.

- 같은이름의 메서드 불가능

- 인터페이스를 상속받는 클래스는 인터페이스안에 있는 메서드를 **모두 오버라이딩 해야함!!**

