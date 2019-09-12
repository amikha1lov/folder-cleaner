#!/usr/bin/gjs

imports.package.init({ name: "folder-cleaner",
                       version: "0.01",
                       prefix: "",
                       libdir: "" });
                       
imports.searchPath.unshift("/home/late/Documents/folder-cleaner");

imports.package.run(imports.src.main);
