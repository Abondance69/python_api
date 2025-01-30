import React from "react";
import { useParams, Link } from "react-router-dom";
import { useGetMovie } from "../../hooks";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart } from "@fortawesome/free-solid-svg-icons/faHeart";

export default function Movie() {
    const { id } = useParams();
    const { data, loading, error } = useGetMovie(id);
    const title = data.title;

    console.log(data);
    console.log(loading);
    console.log(error);

    const src = `${process.env.REACT_APP_MOVIES_IMAGE}/${data.image}`;

    return (
        <div className="h-full min-h-screen max-w-full bg-slate-950 p-4">
            <div className="flex">
                <div className="border">
                    <div className="card-image">
                        <div className="max-w-96 m-2  rounded shadow">
                            <div className="h-5/6">
                                <img
                                    className="w-full h-full object-cover cove"
                                    src={src}
                                    alt="poster"
                                />
                            </div>
                        </div>
                    </div>
                </div>

                <div className="border flex-auto p-4 mx-4">
                    <div className="flex justify-between items-center">
                        <h1 className="text-3xl text-white">
                            {title}{" "}
                            <span className="text-slate-300">(2023)</span>
                        </h1>

                        <FontAwesomeIcon icon={faHeart} className="icon" />
                    </div>

                    <div>
                        <span>25/01/2022(FR)</span>

                        <span className="mx-3">
                            <Link to="/" className="mx-1 text-red-600">
                                Action
                            </Link>
                            <Link to="/" className="mx-1 text-red-600">
                                Comédie
                            </Link>
                            <Link to="/" className="mx-1 text-red-600">
                                Science-Fiction
                            </Link>
                        </span>

                        <span>2h43m</span>
                    </div>
                </div>
            </div>
        </div>
    );
}
