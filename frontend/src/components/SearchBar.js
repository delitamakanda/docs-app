const SearchBar = ({ formSubmit, value, handleSearchKey, clearSearch}) => {
    return (
        <div className="searchBar-wrap">
            <form onSubmit={formSubmit}>
                <input type="text" value={value} onChange={handleSearchKey} className="searchBar" placeholder="Search" />
                {value.length > 0 && <button type="button" onClick={clearSearch} className="clearSearch">Clear</button>}
                <button type="submit" className="searchButton">Search</button>
            </form>
        </div>
    )
}

export default SearchBar