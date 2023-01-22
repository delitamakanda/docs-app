import { useState, React } from 'react';
import EmptyList from '../components/EmptyList';
import Header from '../components/Header';
import BlogList from '../components/BlogList';
import SearchBar from '../components/SearchBar';
import { blogList } from '../config/Api';

const HomePage = ({data}) => {
    const [blogs, setBlogs] = useState([]);
    const [search, setSearch] = useState('');

    const handleSearch = (e) => {
        e.preventDefault();
        handleSearchResults();
    }

    const handleSearchResults = () => {
       // todo
    }
    const handleClearSearch = () => {
        blogList().then((res) => {
            setBlogs(res.data);
        });
        setSearch('');
    }

    const blogContent = (slug) => {
        data(slug);
    }
    
    return (
        <div>
            <Header />
            <SearchBar value={search} formSubmit={handleSearch} clearSearch={handleClearSearch} handleSearchKey={ (e) => setSearch(e.target.value )} />
            {blogs.length > 0 ? <BlogList blogs={blogs} blogContent={blogContent} /> : <EmptyList />}
        </div>
    );
};

export default HomePage;