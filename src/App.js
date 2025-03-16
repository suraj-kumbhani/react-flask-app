import React, { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [title, setTitle] = useState("");
  const [gist, setGist] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    fetch("/api/summary", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url }),
    })
      .then((res) => res.json())
      .then((data) => {
        setTitle(data.title);
        setGist(data.gist);
      });
  }

  return (
    <div className="App">
      <header className="App-header">
        <form className="App" onSubmit={handleSubmit}>
          <label htmlFor="url">
            <pre>Input Your Link:</pre>
            <input
              type="url"
              name="url"
              className="inputurl"
              placeholder="Paste your url here"
              id="url"
              required
              onChange={(e) => setUrl(e.target.value)}
            />
          </label>
          <button type="submit" name="submit">
            Submit
          </button>
        </form>

        {title && (
          <>
            <p>Title: {title}</p>
            <p>Description: {gist}</p>
          </>
        )}
      </header>
    </div>
  );
}

export default App;
