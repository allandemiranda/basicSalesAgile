--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1 (Debian 13.1-1.pgdg100+1)
-- Dumped by pg_dump version 13.1 (Debian 13.1-1.pgdg100+1)

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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: allanmiranda
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO allanmiranda;

--
-- Name: products; Type: TABLE; Schema: public; Owner: allanmiranda
--

CREATE TABLE public.products (
    id integer NOT NULL,
    name character varying NOT NULL,
    value double precision NOT NULL
);


ALTER TABLE public.products OWNER TO allanmiranda;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: allanmiranda
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO allanmiranda;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: allanmiranda
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: sales; Type: TABLE; Schema: public; Owner: allanmiranda
--

CREATE TABLE public.sales (
    id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer NOT NULL,
    total double precision NOT NULL,
    date timestamp without time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.sales OWNER TO allanmiranda;

--
-- Name: sales_id_seq; Type: SEQUENCE; Schema: public; Owner: allanmiranda
--

CREATE SEQUENCE public.sales_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sales_id_seq OWNER TO allanmiranda;

--
-- Name: sales_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: allanmiranda
--

ALTER SEQUENCE public.sales_id_seq OWNED BY public.sales.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: allanmiranda
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying NOT NULL,
    phone character varying NOT NULL,
    user_name character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO allanmiranda;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: allanmiranda
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO allanmiranda;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: allanmiranda
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: sales id; Type: DEFAULT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.sales ALTER COLUMN id SET DEFAULT nextval('public.sales_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: allanmiranda
--

COPY public.alembic_version (version_num) FROM stdin;
bebe66de9de9
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: allanmiranda
--

COPY public.products (id, name, value) FROM stdin;
1	Caneta	12.55
2	Lápis	15.22
3	CPU	144.7
4	Laptop	284.2
5	Galaxy	24.2
\.


--
-- Data for Name: sales; Type: TABLE DATA; Schema: public; Owner: allanmiranda
--

COPY public.sales (id, product_id, quantity, total, date, user_id) FROM stdin;
1	1	3	120.33	2021-01-13 23:11:22.420521	1
2	2	2	10.33	2021-01-13 23:11:38.8948	3
3	3	4	10	2021-01-13 23:11:58.524142	5
4	5	1	99.99	2021-01-13 23:12:25.840276	7
5	5	1	99.99	2021-01-13 23:12:34.622111	1
6	2	7	9.99	2021-01-13 23:12:45.745557	1
7	4	1	77.89	2021-01-13 23:13:08.140079	2
8	4	1	77.89	2021-01-13 23:13:45.129781	3
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: allanmiranda
--

COPY public.users (id, name, phone, user_name, password) FROM stdin;
1	Allan Miranda	+55 84 991151610	allan_miranda	$2b$10$iQH/6uyvm/AMgCzQwS9.eOCd0MsFFPHOaCdSyPd3D66pg3rscAOXi
2	Teste 01	+55 84 991151611	teste_01	$2b$10$8wrAZYD7cjbyuvp/HM5eOugTYu7ymoDn246.wl4XBkFoFMLwiFn4y
3	Teste 02	+55 84 991151612	teste_02	$2b$10$1sTlx8858SVdaXUJZQUDVeniymIJPULJk8daTKizJm7ri9TMsyZ5u
4	Silva 02	+55 84 991151613	silva_02	$2b$10$fnBI95ccc9RcOg9LUtlcM.hQVumaR81I.7V0TcEnGvtsayA9oWu4u
5	Silva 01	+55 84 991151614	silva_01	$2b$10$ebFT49D55Oewe2.yHglice6mHBbVKybLOPFnN1zmjQPLNWrpzYiBa
6	Miranda 01	+55 84 991151616	miranda_01	$2b$10$eI9etlGHSyjMQcI31VYKxu.dbiqz.RNq9N3JErHntVxyYxjL1.gm2
7	Miranda 02	+55 84 991151617	miranda_02	$2b$10$4ivvSTLr1cBLad5VYmcbP.VtTyfoj4ALE8c690lq0qEk3VK.9xkxi
\.


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: allanmiranda
--

SELECT pg_catalog.setval('public.products_id_seq', 5, true);


--
-- Name: sales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: allanmiranda
--

SELECT pg_catalog.setval('public.sales_id_seq', 8, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: allanmiranda
--

SELECT pg_catalog.setval('public.users_id_seq', 7, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: sales sales_pkey; Type: CONSTRAINT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.sales
    ADD CONSTRAINT sales_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_user_name_key; Type: CONSTRAINT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_user_name_key UNIQUE (user_name);


--
-- Name: sales sales_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.sales
    ADD CONSTRAINT sales_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: sales sales_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: allanmiranda
--

ALTER TABLE ONLY public.sales
    ADD CONSTRAINT sales_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

