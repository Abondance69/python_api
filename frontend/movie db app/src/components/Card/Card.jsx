import React from "react";
import { Link } from "react-router-dom";

export default function Card({ data }) {
    const src = `${process.env.REACT_APP_MOVIES_IMAGE}/${data.image}`;

    return (
        <div className="max-w-72 m-2  rounded shadow">
            <div className="h-5/6">
                <Link to={`/movie/${data.id}`}>
                    <img
                        className="w-full h-full object-cover cove"
                        src={src}
                        alt="poster"
                    />
                </Link>
            </div>

            <div className="py-3 pr-3">
                <Link to={`/movie/${data.id}`}>
                    <h5 className="text-lg text-gray-900 dark:text-slate-200">
                        {data.titre}
                    </h5>
                </Link>
            </div>
        </div>
    );
}
