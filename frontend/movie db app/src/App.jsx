import React from "react";
import Navbar from "./components/Navbar/Navbar";
import Playing from "./components/Playing/Playing";
import Popular from "./components/Popular/Popular";
import Comming from "./components/Comming/Comming";
import Rating from "./components/Rating/Rating";
import Movie from "./components/Movie/Movie";
import { BrowserRouter, Routes, Route } from "react-router-dom";

export default function App() {
  return (
    <>
      <BrowserRouter>
        <Navbar />

        <Routes>
          <Route path="/" element={<Playing />}></Route>
          <Route path="/popular" element={<Popular />}></Route>
          <Route path="/upcoming" element={<Comming />}></Route>
          <Route path="/rating" element={<Rating />}></Route>
          <Route path="/movie/:id" element={<Movie />}></Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}
