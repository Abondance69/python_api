import { useEffect, useState } from "react";
import MovieServices from "../services";

export function useGetPlaying() {
    const [datas, setDatas] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        const movieServices = new MovieServices();
        movieServices.getMoviesPlaying()
            .then((resolve) => {
                setLoading(false);
                setDatas(resolve.movies);
                console.log(resolve);
            })
            .catch((error) => {
                setLoading(true);
                setError(false);
                console.log("Une erreur est survenue ", error);
            });
    }, []);

    return {datas, loading, error};
}

export function useGetPopular(){
    const [datas, setDatas] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        const movieServices = new MovieServices();
        movieServices.getMoviesPopular()
            .then((resolve) => {
                setLoading(false);
                setDatas(resolve.movies);
                console.log(resolve);
            })
            .catch((error) => {
                setLoading(true);
                setError(false);
                console.log("Une grosse erreur", error);
            });
    }, []);

    return {datas, loading, error};
}

export function useGetComming(){
    const [datas, setDatas] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        const movieServices = new MovieServices();
        movieServices.getMoviesComming()
            .then((resolve) => {
                setLoading(false);
                setDatas(resolve.movies);
                console.log(resolve);
            })
            .catch((error) => {
                setLoading(true);
                setError(false);
                console.log("Une grosse erreur", error);
            });
    }, []);

    return {datas, loading, error};
}

export function useGetRating(){
    const [datas, setDatas] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        const movieServices = new MovieServices();
        movieServices.getMoviesRating()
            .then((resolve) => {
                setLoading(false);
                setDatas(resolve.movies);
                console.log(resolve);
            })
            .catch((error) => {
                setLoading(true);
                setError(false);
                console.log("Une grosse erreur", error);
            });
    }, []);

    return {datas, loading, error};
}

export function useGetMovie(id){
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);

    useEffect(() => {
        const movieServices = new MovieServices();
        movieServices.getMovieById(id)
            .then((resolve) => {
                setLoading(false);
                setData(resolve);
                console.log(resolve);
            })
            .catch((error) => {
                setLoading(true);
                setError(false);
                console.log("Une grosse erreur", error);
            });
    }, [id]);

    return {data, loading, error};
}

