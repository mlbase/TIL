# ajax 비동기통신 controller로 맵핑하기

```java
	@ResponseBody	// <- Ajax
	@RequestMapping(value = "idcheck.do", method= {RequestMethod.GET,RequestMethod.POST 	}, produces = "application/String; charset=utf-8")
	public String idcheck(String id) {
		logger.info("HomeController idcheck() " + new Date());
		System.out.println("id:"+id);
		
		return "ok";
		
	}
```

- `@ResponseBody` : Ajax로 controller를 맵핑했을 때 return값이 url이 아님으로 반드시 붙여줘야한다.

- `produces = "application/String; charset=utf-8"` : Ajax로 넘어온 값은 utf-8성질을 안가짐으로 한글을 사용할 경우 반드시 utf-8로 전환해줘야함

