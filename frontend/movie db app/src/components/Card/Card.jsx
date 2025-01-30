import React, { useState } from "react";
import { Link } from "react-router-dom";

export default function Card({ data }) {
  const [loading, setLoading] = useState(true);
  const src = `${process.env.REACT_APP_MOVIES_IMAGE}/${data.image}`;

  const handleImageLoad = () => {
    setLoading(false);
  };

  return (
    <div className="max-w-72 m-2 rounded shadow overflow-hidden">
      <div className="h-5/6 relative">
        <Link to={`/movie/${data.id}`}>
          <img
            className={`w-full h-full object-cover ${
              loading ? "opacity-0" : "opacity-100"
            }`}
            src={src}
            alt="poster"
            onLoad={handleImageLoad}
            loading="lazy"
          />
          {loading && (
            <div className="absolute inset-0 bg-gray-200 opacity-75 animate-pulse">
              <div className="w-full h-full bg-gray-300"></div>
            </div>
          )}
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
