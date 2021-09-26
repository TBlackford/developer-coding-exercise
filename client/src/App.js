import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import PostListPage from './pages/PostListPage';
import PostPage from './pages/PostPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={PostListPage} />
        <Route path="/:slug" component={PostPage} />
      </Switch>
    </Router>
  );
}

export default App;
