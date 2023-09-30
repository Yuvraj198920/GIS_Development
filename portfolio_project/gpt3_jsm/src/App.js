import React from "react";
import { Article, Brand, CTA, Navbar } from "./components";
import { Blog, Features, Footer, Header, Possibility, WhatGPT3 } from './containers';

export default function App() {
    return (
        <div className="App">
            <div className="gradient_bg">
                <Navbar />
                <Header />
            </div>
       
           <Brand />
           <WhatGPT3 />
           <Features/>
           <Possibility />
           <CTA />
           <Blog />
           <Footer />
        </div>
    )
}