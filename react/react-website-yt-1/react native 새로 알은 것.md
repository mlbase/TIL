# react native 새로 알은 것

- html 의 경우 `<a href to='주소'>` 로 할수 있지만 react에서는 `<Link to '/about' >소개 </Link>`로 나타낸다

  

# react router [링크주소참조](https://reactrouter.com/web/guides/quick-start)

```react
import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

export default function App() {
  return (
    <Router> 
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link> 
                /*to속성에 설정된 링크로 이동. 기록이 history스택에 저장 */
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav>

        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
            /*oute또는 Redirect중 매치되는 첫 번째 요소를 렌더링합니다. Switch를 사용하면 BrowserRouter만 사용할 때와 다르게 하나의 매칭되는 요소만 렌더링한다는 점을 보장해줍니다.
사용하지 않을 경우 매칭되는 모두를 렌더링합니다.*/
          <Route path="/about">
              /* 컴포넌트의 속성에 설정된 URL과 현재 경로가 일치하면 해당하는 컴포넌트, 함수를 렌더링 */
            <About />
          </Route>
          <Route path="/users">
            <Users />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

function Home() {
  return <h2>Home</h2>;
}

function About() {
  return <h2>About</h2>;
}

function Users() {
  return <h2>Users</h2>;
}
```

