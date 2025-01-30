import React from "react";
import Card from "../Card/Card";
import Loader from "../Loader/Loader";
import {useGetPlaying} from "../../hooks";

export default function Playing() {
    const {datas, loading, error} = useGetPlaying();

    let content = "";

    if (loading) {
        content = <Loader />
    } else if (error) {
        content = <p>Une erreur est survenue</p>;
    } else if (datas) {
        content = datas.map((data, index) => (
            <Card key={index} data={data} />
        ));
    }

    return (
        <div className="h-full min-h-screen max-w-full bg-slate-950 p-4">
            <div className="max-w-7xl mx-auto flex flex-wrap justify-center">
                {content}
            </div>
        </div>
    );
}
