import React from 'react';
import { Router } from '@reach/router';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Main from './views/Main';
import Wrapper from './components/Wrapper';

function App() {
  return (
    <div className="App">
      <Wrapper>
        <Router>
          <Main path='/' />
        </Router>
      </Wrapper>
    </div>
  );
}

export default App;
