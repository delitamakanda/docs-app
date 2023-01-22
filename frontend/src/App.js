import './App.css';
import { Routes, Route } from 'react-router-dom';
import { React, useState } from 'react';
import HomePage from './pages/HomePage';
import BlogPost from './pages/BlogPost';

function App() {
  const [posts, setPosts] = useState([]);
  const getPosts = async (blog) => {
    setPosts(blog);
  }
  return (
    <div className='container'>
      <Routes>
        <Route path='/' element={<HomePage getPosts={getPosts} />} />
        <Route path='/blog/:slug' element={<BlogPost getPosts={posts} />} />
      </Routes>
    </div>
  );
}

export default App;
