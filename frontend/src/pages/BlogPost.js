import { React } from 'react';
import Chip from '../components/Chip';
import EmptyList from '../components/EmptyList';
import { Link } from'react-router-dom';
import '../index.css';
const BlogPost = () => {

    return (
        <>
            <Link className='back' to='/'>
                <Chip label="Go" />
                <EmptyList />
            <span>&#8592;</span><span>Go back</span>
            </Link>
        </>
    )
}

export default BlogPost