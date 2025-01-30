import React from "react";
import { useGetComming } from "../../hooks";
import Card from "../Card/Card";
import Loader from "../Loader/Loader";

export default function Comming() {
    const { datas, loading, error } = useGetComming();

    let content = "";

    if (loading) {
        content = <Loader />;
    } else if (error) {
        content = <p>Une erreur est survenue</p>;
    } else if (datas) {
        content = datas.map((data, index) => <Card key={index} data={data} />);
    }

    return (
        <div className="h-full min-h-screen max-w-full bg-slate-950 p-4">
            <div className="max-w-7xl mx-auto flex flex-wrap justify-center">
                {content}
            </div>
        </div>
    );
}
