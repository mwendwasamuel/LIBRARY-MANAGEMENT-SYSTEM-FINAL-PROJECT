import React, { Component } from 'react';

class Search extends Component {
  constructor(props) {
    super(props);
    this.state = {
      books: [],   // Array to store book data
      search: '',  // Search input value
    };
  }

  componentDidMount() {
    // Fetch book data from the Flask API endpoint
    fetch('/api/books')
      .then((res) => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then((books) => this.setState({ books }))
      .catch((error) => console.error('Error fetching books:', error));
  }

  // Handle search input change
  handleChange = (e) => {
    this.setState({ search: e.target.value });
  };

  render() {
    const { search, books } = this.state;

    // Filter books based on the search input
    const filteredBooks = books.filter((book) => {
      // Check if the search input matches any book title, category, author, or ISBN
      const searchTerm = search.toLowerCase();
      return (
        book.Name.toLowerCase().includes(searchTerm) ||
        book.Category.toLowerCase().includes(searchTerm) ||
        book.Author.toLowerCase().includes(searchTerm) ||
        book.ISBN.toLowerCase().includes(searchTerm)
      );
    });

    return (
      <div className="container">
        <h2>&nbsp;</h2>
        <input
          className="form-control col-sm-2"
          type="text"
          onChange={this.handleChange}
          placeholder="Search Books"
          value={search} // Controlled input value
        />
        <h2>&nbsp;</h2>
        <h1>Your Searched Books</h1>
        <table className="table table-hover">
          <thead>
            <tr>
              <th>Serial</th>
              <th>Name</th>
              <th>Category</th>
              <th>Author</th>
              <th>ISBN</th>
            </tr>
          </thead>
          <tbody>
            {filteredBooks.map((bookItem) => (
              <tr key={bookItem.ISBN}>
                <td>{bookItem.Serial}</td>
                <td>{bookItem.Name}</td>
                <td>{bookItem.Category}</td>
                <td>{bookItem.Author}</td>
                <td>{bookItem.ISBN}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default Search;
