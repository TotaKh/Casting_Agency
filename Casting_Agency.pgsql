--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: taghreed
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying,
    age integer,
    gender character varying
);


ALTER TABLE public.actors OWNER TO taghreed;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: taghreed
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO taghreed;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taghreed
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: taghreed
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO taghreed;

--
-- Name: movies; Type: TABLE; Schema: public; Owner: taghreed
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying,
    release character varying,
    actor character varying
);


ALTER TABLE public.movies OWNER TO taghreed;

--
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: taghreed
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO taghreed;

--
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taghreed
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: taghreed
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: taghreed
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: taghreed
--

COPY public.actors (id, name, age, gender) FROM stdin;
1	Millie Brown	17	Female
2	Jesse Eisenberg	37	Male
3	Robert Downey	55	Male
4	Leonardo DiCaprio	46	Male
5	Selena Gomez	28	Female
6	Adam Sandler	54	Male
7	Jennifer Aniston	52	Female
8	Will Smith	52	Male
9	Yifei Liu	33	Female
10	Anna Kendrick	35	Female
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: taghreed
--

COPY public.alembic_version (version_num) FROM stdin;
1f2a2252ff39
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: taghreed
--

COPY public.movies (id, title, release, actor) FROM stdin;
1	Enola Holmes	2020	Millie Brown
2	Now You See Me	2013	Jesse Eisenberg
3	Iron Man	2008	Robert Downey
4	The Great Gatsby	2013	Leonardo DiCaprio
5	Monte Carlo	2011	Selena Gomez
6	Murder Mystery	2019	Adam Sandler
7	We re the Millers	2013	Jennifer Aniston
8	Focus	2015	Will Smith
9	Mulan	2020	Yifei Liu
10	Pitch Perfect	2012	Anna Kendrick
11	Inception	2010	Leonardo DiCaprio
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taghreed
--

SELECT pg_catalog.setval('public.actors_id_seq', 15, true);


--
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taghreed
--

SELECT pg_catalog.setval('public.movies_id_seq', 8, true);


--
-- Name: actors actors_name_key; Type: CONSTRAINT; Schema: public; Owner: taghreed
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_name_key UNIQUE (name);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: taghreed
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: taghreed
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: taghreed
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- Name: movies movies_actor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: taghreed
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_actor_fkey FOREIGN KEY (actor) REFERENCES public.actors(name);


--
-- PostgreSQL database dump complete
--

