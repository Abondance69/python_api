export default class MovieServices {
  async getMoviesPlaying() {
    const url = `${process.env.REACT_APP_URL_API_SITE}/api/movie/now_playing`;

    try {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          accept: "application/json",
        },
      });

      if (!response.ok) {
        throw new Error("Une autre erreur detectée");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.log("Une erreur est survenue", error);
    }
  }

  async getMoviesPopular() {
    const url = `${process.env.REACT_APP_URL_API_SITE}/api/movie/popular`;

    try {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          accept: "application/json",
          Authorization: `Bearer ${process.env.REACT_APP_API_JETON_KEY}`,
        },
      });

      if (!response.ok) {
        throw new Error("Une autre erreur detectée");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.log("Une erreur est survenue", error);
    }
  }

  async getMoviesComming() {
    const url = `${process.env.REACT_APP_URL_API_SITE}/api/movie/upcoming`;

    try {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          accept: "application/json",
          Authorization: `Bearer ${process.env.REACT_APP_API_JETON_KEY}`,
        },
      });

      if (!response.ok) {
        throw new Error("Une autre erreur detectée");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.log("Une erreur est survenue", error);
    }
  }

  async getMoviesRating() {
    const url = `${process.env.REACT_APP_URL_API_SITE}/api/movie/top_rated`;

    try {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          accept: "application/json",
          Authorization: `Bearer ${process.env.REACT_APP_API_JETON_KEY}`,
        },
      });

      if (!response.ok) {
        throw new Error("Une autre erreur detectée");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.log("Une erreur est survenue", error);
    }
  }

  async getMovieById(id) {
    const url = `${process.env.REACT_APP_URL_API_SITE}/api/movie/${id}`;

    try {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          accept: "application/json",
          Authorization: `Bearer ${process.env.REACT_APP_API_JETON_KEY}`,
        },
      });

      if (!response.ok) {
        throw new Error("Une autre erreur detectée");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.log("Une erreur est survenue", error);
    }
  }
}