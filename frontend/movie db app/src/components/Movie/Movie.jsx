import React from "react";
import { useParams, Link } from "react-router-dom";
import { useGetMovie } from "../../hooks";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart } from "@fortawesome/free-solid-svg-icons/faHeart";

export default function Movie() {
  const { id } = useParams();
  const { data, loading, error } = useGetMovie(id);
  const title = data.titre ?? "";
  const date_sortie = data.date_sortie ?? "";
  const src = `${process.env.REACT_APP_MOVIES_IMAGE}/${data.image}`;

  return (
    <div className="h-full min-h-screen max-w-full bg-slate-950 p-4">
      <div className="flex flex-col md:flex-row items-center md:items-start">
        <div className="card-image max-h-96 m-2 rounded-lg overflow-hidden shadow-lg">
          <img
            className="w-full h-full object-cover rounded-lg transform scale-105 transition-all duration-300"
            src={src}
            alt="poster"
          />
        </div>

        <div className="flex flex-col justify-center p-4 mx-4 text-center md:text-left">
          <h1 className="text-3xl text-white font-semibold mb-2">{title}</h1>

          <div className="text-lg text-slate-300 mb-4">
            <span>Date de sortie : {date_sortie}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
