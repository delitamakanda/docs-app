import BlogItem from "./BlogItem";
import '../index.css';

const BlogList = ({ blogs, content }) => {
    return (
        <div>
            {blogs.map((blog) => (
                <BlogItem key={blog.id} blog={blog} content={content} />
            ))}
        </div>
    )
}

export default BlogList;
