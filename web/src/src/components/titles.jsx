import React, {useEffect, useState} from "react";
import axios from "axios";

const PAGE_SIZE = 20;

const Titles = () => {
    const [titles, setTitles] = useState();
    const [page, setPage] = useState(0);

    useEffect(() => {
        axios.get(`/api/titles?_page=${page}&_limit=${PAGE_SIZE}`)
        .then(res => {
            setTitles(res.data);
        });
    }, [page]);

    function onClick() {
        axios.get(`/api/titles?_page=${page}&_limit=${PAGE_SIZE}`)
            .then(res => {
                setTitles(res.data);
            });
    }

    return <div>{
        !titles ? ('No data found') : (
            <table className='table'>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Title number</th>
                        <th>Title class</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        titles.map((title, index) => 
                            <tr key={index}>
                                <td>{title.id}</td>
                                <td>{title.title_number}</td>
                                <td>{title.title_class}</td>
                            </tr>
                        )
                    }
                </tbody>
            </table>)
        }
        <nav className="d-flex justify-content-center">
            <ul className="pagination">
                {
                    page > 0 ? <button onClick={() => { setPage(page - 1); onClick() }} className="page-link">Back to page {page - 1}</button> : ''
                }
                <button onClick={() => { setPage(page + 1); onClick() }} className="page-link">Go to page {page + 1}</button>
            </ul>
        </nav>
    </div>
}

export default Titles;
