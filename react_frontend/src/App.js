import './App.css';
import Header from './components/Header';
import {UsersListPage} from './pages/UsersListPage';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <Header/>
      <UsersListPage/>
    </div>
  );
}

export default App;
