# jquery

### 접근

- $(태그명/클래스명/id이름).처리메서드()

- class가 중복 될때 값을 그냥 가져올경우 문자열로 붙여서 가져온다. 따라서 `each()`를 사용해서 가져옴. (class 이름이 같더라도 주소는 다르기 때문에 `.this`활용)

- ready method는 html파일이 모두 로딩된 이후 작동된다.

- `html(), text(), val(), css(), attr(), prop()`

  ---

### input tag 접근

```javascript
//getter
let rVal = $("input[name='radio_test']:checked").val();
alert(rVal);
//setter
		$("input[name='radio_test']").val(["banana"]);
```

### tag 추가

1. `html(text)` 추가

```javascript
let txt = "<p><b>html p tag Append</b></p>";
$("#demo").append(txt);
```



---

2. *javascript* 추가

```javascript
let element = document.createElement("h3");
element.innerHTML = "JS h3 tag append";
$("#demo").append(element);
```



---

3. JQuery 추가

   ```javascript
   let element = $("<p></p>").html("JQuery p tag append");
   $('#demo').append(element);
   ```

   

### `attr()`메서드

---

1.  tag 의 속성 **attribute  **를 js로 가져올 수 있음 

   ex>

   ```javascript
   let id = $("p").attr("id");
   ```

   

2. tag의 속성 *attribute*를 변경이나 추가 가능

   ex) ```

   ```javascript
   $('p').attr("id",'one');
   ```

   

   

   

